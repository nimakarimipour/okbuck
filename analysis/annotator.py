import subprocess
import os

REPO = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip().decode('utf-8')
OUT_DIR = '{}/annotator-out'.format(REPO)
ANNOTATOR_JAR = "{}/jars/annotator-core-1.3.14.jar".format(REPO)


def prepare():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open('{}/paths.tsv'.format(OUT_DIR), 'w') as o:
        o.write("{}\t{}\n".format('{}/nullaway.xml'.format(OUT_DIR), '{}/scanner.xml'.format(OUT_DIR)))
    os.system("rm -rvf ../annotator-out/0 > /dev/null 2>&1")


def run_annotator():
    prepare()
    commands = []
    commands += ["java", "-jar", ANNOTATOR_JAR]
    commands += ['-d', OUT_DIR]
    commands += ['-bc', 'cd {} && ./annotator-command.sh'.format(REPO)]
    commands += ['-cp', '{}/paths.tsv'.format(OUT_DIR)]
    commands += ['-i', 'com.uber.nullaway.annotation.Initializer']
    commands += ['-n', 'javax.annotation.Nullable']
    commands += ['-cn', 'NULLAWAY']
    commands += ["--depth", "25"]
    # Uncomment to see build output
    # commands += ['-rboserr']
    # Comment to inject root at a time
    # commands += ['-ch']
    # Uncomment to disable cache
    # commands += ['-dc']
    # Uncomment to disable outer loop
    # commands += ['-dol']
    # Uncomment to disable parallel processing
    # commands += ['--disable-parallel-processing']
    # Uncomment to suppress remaining errors
    # commands += ["--suppress-remaining-errors", "org.jspecify.annotations.NullUnmarked"]
    print(commands)

    subprocess.call(commands)


run_annotator()

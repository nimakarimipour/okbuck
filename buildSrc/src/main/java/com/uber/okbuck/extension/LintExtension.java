package com.uber.okbuck.extension;

import com.uber.okbuck.core.annotation.Experimental;
import com.uber.okbuck.core.manager.LintManager;
import org.gradle.api.Project;
import javax.annotation.Nullable;

@Experimental
public class LintExtension {

  /** Lint jar version */
  @Nullable @SuppressWarnings("CanBeFinal")
  public String version;

  /** Set to {@code true} to disable generation of lint rules */
  public boolean disabled = false;

  /** JVM arguments when invoking lint */
  public String jvmArgs = "-Xmx1024m";

  LintExtension(Project project) {
    version = LintManager.getDefaultLintVersion(project);
  }
}

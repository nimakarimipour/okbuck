package com.uber.okbuck.extension;

import com.uber.okbuck.core.manager.KotlinManager;
import org.gradle.api.Project;
import javax.annotation.Nullable;

public class KotlinExtension {

  /** Version of the kotlin compiler to use. */
  @Nullable @SuppressWarnings("CanBeFinal")
  public String version;

  KotlinExtension(Project project) {
    version = KotlinManager.getDefaultKotlinVersion(project);
  }
}

package com.uber.okbuck.extension;

import com.uber.okbuck.core.manager.KotlinManager;
import javax.annotation.Nullable;
import org.gradle.api.Project;

public class KotlinExtension {

  /** Version of the kotlin compiler to use. */
  @Nullable @SuppressWarnings("CanBeFinal")
  
  public String version;

  KotlinExtension(Project project) {
    version = KotlinManager.getDefaultKotlinVersion(project);
  }
}

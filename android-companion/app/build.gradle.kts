plugins {
    id("com.android.application")
}

android {
    namespace = "com.sodrius.nebli.companion"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.sodrius.nebli.companion"
        minSdk = 26
        targetSdk = 35
        versionCode = 5
        versionName = "0.3.2"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
}

dependencies {
    implementation("androidx.core:core:1.15.0")
    testImplementation("junit:junit:4.13.2")
}

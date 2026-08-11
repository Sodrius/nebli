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
        versionCode = 2
        versionName = "0.2.0"
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
    testImplementation("junit:junit:4.13.2")
}

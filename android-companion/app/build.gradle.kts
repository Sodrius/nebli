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
        versionCode = 13
        versionName = "0.8.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
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
    androidTestImplementation("androidx.test:runner:1.6.2")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
}

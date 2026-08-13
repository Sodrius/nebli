# Nebli Companion 0.8.0

Instala manifestos `nebli-ankidroid-deck-v3` diretamente no AnkiDroid oficial. O modo canônico `authored_only` aceita cards autorais e Image Occlusion, valida a versão mínima, hashes, mídia, contagem, deck e recibo, evita duplicação e reverte notas novas em falha.

Build local: `gradle :app:testDebugUnitTest :app:assembleDebug :app:assembleDebugAndroidTest`. O workflow executa também o teste instrumentado contra o APK oficial do AnkiDroid 2.24.0 e publica `app-debug.apk`.

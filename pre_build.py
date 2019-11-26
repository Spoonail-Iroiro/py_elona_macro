import shutil

#srcディレクトリのconfig.jsonを上階層にコピー（アプリ階層と同じ）
shutil.copy("config.json", "../config.json")
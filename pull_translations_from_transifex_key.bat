echo "Pulling localisation files from Transifex"
:: Force pull all translations
tx.exe pull --all --force -translations
::pause
python merge_key.py

pause
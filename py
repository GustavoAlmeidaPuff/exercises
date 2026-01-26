#!/bin/bash
# Script wrapper para executar Python com o comando 'py'
# Uso: py arquivo.py ou ./py arquivo.py
# Este script tem prioridade sobre o /usr/bin/py do pythonpy quando o diretório está no PATH
python3 "$@"

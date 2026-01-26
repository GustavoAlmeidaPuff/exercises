#!/bin/bash
# Script para adicionar o diretório atual ao PATH temporariamente
# Uso: source setup-py.sh ou . setup-py.sh

export PATH="$PWD:$PATH"
echo "Diretório atual adicionado ao PATH. Agora você pode usar 'py 021.py'"

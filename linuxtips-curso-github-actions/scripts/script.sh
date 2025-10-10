#!/usr/bin/env bash
# script.sh

echo "=== Resultado do Script ===" > resultado.txt
echo "Data de execução: $(date '+%Y-%m-%d %H:%M:%S')" >> resultado.txt
echo "Hostname: $(hostname)" >> resultado.txt
echo "Usuário atual: $(whoami)" >> resultado.txt
echo "Diretório atual: $(pwd)" >> resultado.txt
echo "-----------------------------" >> resultado.txt

echo "Arquivo resultado.txt criado com sucesso!"

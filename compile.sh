#!/usr/bin/env bash

TMP_DIR='tmp'
OUT_DIR='.'

show_help() {
    echo -e "usage: $(basename "$0") [-h] [-t]\n\nOptional arguments:\n\t-h\t\tShow this help message and exit\n\t-t\t\tTemporary directory path [Default: $TMP_DIR]\n\t-o\t\tOutput directory path [Default: $OUT_DIR]"
}

while getopts "t:o:h" opt; do
    case "$opt" in
        t) TMP_DIR=$OPTARG;;
        o) OUT_DIR=$OPTARG;;
        h) show_help; exit 0;;
        ?) show_help; exit 1;;
    esac
done

mkdir -p $TMP_DIR $OUT_DIR
wordz -p src/classes/passwords.py::BasicPasswords -t $TMP_DIR -o $OUT_DIR && \
wordz -p src/classes/passwords.py::ExtendedPasswords -t $TMP_DIR -o $OUT_DIR && \
wordz -p src/classes/dns.py::Subdomains -t $TMP_DIR -o $OUT_DIR && \
wordz -p src/classes/http.py::FileExtensions -t $TMP_DIR -o $OUT_DIR && \
wordz -p src/classes/http.py::HttpWordsPlainCommon -t $TMP_DIR -o $OUT_DIR && \
wordz -p src/classes/http.py::HttpWordsObjectsCommon -t $TMP_DIR -o $OUT_DIR && \
wordz -p src/classes/http.py::HttpWordsSuffixesCommon -t $TMP_DIR -o $OUT_DIR && \
wordz -p src/classes/http.py::HttpWordsDoubleCommon -t $TMP_DIR -o $OUT_DIR

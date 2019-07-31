#!/bin/sh
FIX_CSV_CMD=`pwd`/fix_csv.py
cd $1
echo "commit_hash,author_name,author_email,author_date,committer_name,committer_email,committer_date,subject"
git log --pretty=format:%H,%an,%ae,%ai,%cn,%ce,%ci,%s | ${FIX_CSV_CMD} 8

#!/bin/sh

if [ $# -ne 1 ]
then
	echo "Usage: $0 <out_file>"
	exit 1
fi

echo "Stop recording using Ctrl+C ..."
rec -c 1 $1

echo "Audio Info:"
soxi $1

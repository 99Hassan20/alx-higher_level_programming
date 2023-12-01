#! /usr/bin/env bash
#gets the size of the content
curl -s -w '%{size_download}\n' -o /dev/null $1

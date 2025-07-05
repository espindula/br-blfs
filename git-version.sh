#!/bin/sh

if [ "$1" = sysv ]; then
    SYSV="INCLUDE"
    SYSTEMD="IGNORE "
elif [ "$1" = systemd ]; then
    SYSV="IGNORE "
    SYSTEMD="INCLUDE"
else
    echo You must provide either \"sysv\" or \"systemd\" as argument
    exit 1
fi

echo "<!ENTITY % sysv    \"$SYSV\">"     >  conditional.ent
echo "<!ENTITY % systemd \"$SYSTEMD\">"  >> conditional.ent

if ! git status > /dev/null; then
    # Either it's not a git repository, or git is unavailable.
    # Just workaround.
    echo "<!ENTITY year              \"????\">"            >  version.ent
    echo "<!ENTITY version           \"unknown\">"         >> version.ent
    echo "<!ENTITY releasedate       \"unknown\">"         >> version.ent
    echo "<!ENTITY pubdate           \"unknown\">"         >> version.ent
    exit 0
fi

export LC_ALL=pt_BR.utf8
export TZ=America/Recife

commit_date=$(git show -s --format=format:"%cd" --date=local)
short_date=$(date --date "$commit_date" "+%Y-%m-%d")

year=$(date --date "$commit_date" "+%Y")
month=$(date --date "$commit_date" "+%B")
day_digit=$(date --date "$commit_date" "+%d")
day=$(echo $day_digit | sed 's/^0//')

case $day in
    "1" ) suffix="º";;
    "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ) prefix="0";;
esac

full_date="$prefix$day$suffix de $month de $year"

sha="$(git describe --abbrev=1)"
version=$(echo "$sha" | sed 's/-g[^-]*$//')

if [ "$(git diff HEAD | wc -l)" != "0" ]; then
    version="$version-wip"
fi

echo "<!ENTITY year              \"$year\">"               >  version.ent
echo "<!ENTITY version           \"$version\">"            >> version.ent
echo "<!ENTITY releasedate       \"$full_date\">"          >> version.ent
echo "<!ENTITY pubdate           \"$short_date\">"         >> version.ent

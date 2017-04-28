USER=ytyaru
DESCRIPTION="説明文。"
HOMEPAGE=http://abc
PATH_THIS=$(cd $(dirname $0) && pwd)
PATH_SCRIPT=~/automation/GitHubUploader/hup.py
python3 "${PATH_SCRIPT}" "${PATH_THIS}" -u ${USER} -d "${DESCRIPTION}" -l "${HOMEPAGE}"


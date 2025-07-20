STATIC_TYPING_PYTHON_VERSION=3.12
FAIL_THRESHOLD=100
MAIN_BRANCH=main
MYPY_ARGS="--explicit-package-bases --strict --follow-imports=silent --check-untyped-defs --disallow-untyped-calls --disallow-untyped-defs --warn-unused-ignores --warn-return-any --python-version ${STATIC_TYPING_PYTHON_VERSION}"

mypy $MYPY_ARGS --cobertura-xml-report mypy_report --no-error-summary . || echo "ignore errors"

diff-cover mypy_report/cobertura.xml --compare-branch origin/$MAIN_BRANCH  --fail-under=$FAIL_THRESHOLD

name: strong stock screening

on:
  schedule:
    - cron: '0 21 30 * *'
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: install python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: install libs
        run: pip install pandas requests numpy

      - name: run screening
        env:
          JQUANTS_REFRESH_TOKEN: ${{ secrets.JQUANTS_REFRESH_TOKEN }}
        run: python strong_stock.py

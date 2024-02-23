# MTrade Front

[![CircleCI](https://circleci.com/gh/Cicada-Technologies-Inc/mtrade-frontend-cicada/tree/develop.svg?style=svg&circle-token=b57158d70eb9bc50fad75c4e9f62a53fd6e32d92)](https://circleci.com/gh/Cicada-Technologies-Inc/mtrade-frontend-cicada/tree/develop)

## General Information

- [run project](#to-run-project)
- [run storybook](#to-run-storybook)
- test
  - e2e
    - [cypress console](#to-check-without-browser)
    - [cypress browser](#to-check-with-browser)
  - unit
    - [jest](#to-check-unit-test-with-jest)
    - [jest coverage](#to-check-unit-test-with-coverage)
- config environment
  - [environment variables](#environment-variables)
  - [vscode extensions](#vscode-extensions)
- guidelines
  - [how to name commits/branches](https://www.notion.so/mtrade/How-to-name-branches-and-commits-49e1c7cd5f8f4a9cbc54124254e0ec0e)
  - [PR workflow](https://www.notion.so/mtrade/How-to-work-with-PR-s-bbef12ef701a40f18af2147eb8e6544f#5c410c9821e140868585c3dd6cec0900)

## Overview

This is the frontend repo for CRISPA AI gui 

**Development branch**: `develop`

**Production branch: will be**: `master`

## Environmental variables

[link](#environment-variables)

## To run project

```
feel free to use npm or yarn to execute scripts like `npm run ...`
but be careful to don't use `npm install`, `npm update` or `npm remove` to not generate a package-lock.json and just have yarn.lock
```

1. install dependencies using `node`
2. [connect BE for FE development](https://www.notion.so/mtrade/Connecting-to-Design-QA-and-FE-development-remote-environments-76ce9aefc40346b98e1af3d8e355d408)

   2.1 search `backend-for-fe-development` and config the connection

   2.2 run backend on local port `ssh -N backend-for-fe-development`

3. run in development: `npm run dev` or `yarn dev`
4. open browser [http://localhost:3000](http://localhost:3000`)

## To run Storybook

`npm run storybook` or `yarn storybook`

## To check e2e test with Cypress

### to check without browser

`npm run e2e-mtrade:run` or `yarn e2e-mtrade:run`

### to check with browser

`npm run e2e-mtrade:watch` or `yarn e2e-mtrade:watch`

## To check unit test with Jest

`npm run test` or `yarn test`

### to check unit test with coverage

`npm run test:unit-coverage` or `yarn test:unit-coverage`

# Environmental variables

It's possible create Environmental variables for global projects or for each single application (mtrade/vision)

For global create an `.env` file in root directory with following variables (example values are provided):

```
DOMAIN=127.0.0.1
PORT=9601
NEXT_PUBLIC_HOST=http://$DOMAIN:$PORT

```

For mtrade, create an `.env` file in root mtrade directory (apps/mtrade/) with following variables (example values are provided):

```
DOMAIN=127.0.0.1
PORT=9601
NEXT_PUBLIC_HOST=http://$DOMAIN:$PORT
NEXT_PUBLIC_WEBSOCKET=true
HIDE_2FA=true
FEATURE_FLAG_VERSION=1.1
```

for check choices **_FEATURE_FLAG_VERSION_** check this file `libs\ui-shared\src\functions\featureFlags.ts`

# Config environment

## vscode extensions

- Install `ESLint`(dbaeumer.vscode-eslint) extension on Vscode for checking type issues automatically.
- Install `Sonar linter`(sonarsource.sonarlint-vscode) extension on vscode for quality code checking

## Checking type and formatting

To check type and format manully, should run below commands.
these commands will be run automatically in commiting on git.

### To check type issues

Run command `npm run type-check` or `yarn type-check`

### To format code automatically

Run command `npm run lint-fix` or `yarn lint-fix`

# Launch in production mode

```
yarn nx build && yarn nx serve
```
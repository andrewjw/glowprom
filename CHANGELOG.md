# CHANGELOG

<!-- version list -->

## v1.2.1 (2026-01-21)

### Bug Fixes

- Fix typo in state timestamp metric
  ([`5cd6dbb`](https://github.com/andrewjw/glowprom/commit/5cd6dbb0ff8bec3230e6bf69a61839ddf720dac4))

- More typos fixed.
  ([`9ce6fc3`](https://github.com/andrewjw/glowprom/commit/9ce6fc39214502aeafde4c09b2ddc181e1d5e1fc))


## v1.2.0 (2026-01-19)

### Features

- Add support for the state message and report versions, rssi and lqi. (fixes #156)
  ([`d15c0ec`](https://github.com/andrewjw/glowprom/commit/d15c0ec4907849ac5ee11020a371e2b76e4bcc44))


## v1.1.1 (2026-01-16)

### Bug Fixes

- Fix python_requires in setup.py
  ([`355a7b7`](https://github.com/andrewjw/glowprom/commit/355a7b7f33e5607962a7c42dec724f257d44a80e))

### Chores

- Switch to using black for code style. ([#154](https://github.com/andrewjw/glowprom/pull/154),
  [`5d4c77a`](https://github.com/andrewjw/glowprom/commit/5d4c77a110cf0d03fe469da8a201383dd200e9bb))


## v1.1.0 (2026-01-16)

### Chores

- Add support for Python 3.13 and drop Python 3.8.
  ([#101](https://github.com/andrewjw/glowprom/pull/101),
  [`12e40f0`](https://github.com/andrewjw/glowprom/commit/12e40f0baefb75b358e813aae7dd53f71556dc0c))

- Fix code coverage across multiple Python versions.
  ([#101](https://github.com/andrewjw/glowprom/pull/101),
  [`12e40f0`](https://github.com/andrewjw/glowprom/commit/12e40f0baefb75b358e813aae7dd53f71556dc0c))

- Mark coverage submission as allowed to fail.
  ([#101](https://github.com/andrewjw/glowprom/pull/101),
  [`12e40f0`](https://github.com/andrewjw/glowprom/commit/12e40f0baefb75b358e813aae7dd53f71556dc0c))

- Update coverage to support Python 3.13. ([#101](https://github.com/andrewjw/glowprom/pull/101),
  [`12e40f0`](https://github.com/andrewjw/glowprom/commit/12e40f0baefb75b358e813aae7dd53f71556dc0c))

- **config**: Migrate config renovate.json ([#133](https://github.com/andrewjw/glowprom/pull/133),
  [`fd2cb5b`](https://github.com/andrewjw/glowprom/commit/fd2cb5b5e5201ac9249c4cfcf695dcb5e13a33c2))

### Features

- Drop support for Python 3.9 and add 3.14
  ([`fd4612a`](https://github.com/andrewjw/glowprom/commit/fd4612ad30c5a8ed20015253964bb6dc02299789))


## v1.0.0 (2025-05-29)

### Features

- Remove support for Python 3.8.
  ([`269780a`](https://github.com/andrewjw/glowprom/commit/269780a22d417d6ea19f7016e842ddc484ef7089))

### Breaking Changes

- Remove support for Python 3.8.


## v0.9.0 (2024-08-17)

### Bug Fixes

- Use piwheels.org and Python 3.11 to fix armv7 build.
  ([`899f9fd`](https://github.com/andrewjw/glowprom/commit/899f9fd512b99a279d60b1d973ad66bf698ca319))

### Chores

- Add grafana dashboard ([#77](https://github.com/andrewjw/glowprom/pull/77),
  [`fb7b4c7`](https://github.com/andrewjw/glowprom/commit/fb7b4c731e4253c0e89d72b14c40743daeef242e))

- Add time since last update to Grafana dashboard.
  ([`36b8265`](https://github.com/andrewjw/glowprom/commit/36b82659cfdd71e014b696464a63cd4f934fbfb3))

### Features

- Install a local .tar.gz in docker to allow testing and more reliable releases.
  ([`4254779`](https://github.com/andrewjw/glowprom/commit/4254779caba571342f3aba65ba96f13f98a220b2))


## v0.8.0 (2024-07-09)

### Bug Fixes

- Fix docker push by logging in if we're pushing.
  ([`6c18e01`](https://github.com/andrewjw/glowprom/commit/6c18e017a347e9fb25767fcf88373c515656a5cc))

- Only build docker once, after all Python versions are tested.
  ([`1377c07`](https://github.com/andrewjw/glowprom/commit/1377c073441e1f7ec2075614df777aad17a1fe2e))

- Setup tools has been removed in Python 3.12.
  ([`8818f91`](https://github.com/andrewjw/glowprom/commit/8818f911ef1078485d308797a4872e3bddca601b))

- Try to find rust compiler.
  ([`32d438c`](https://github.com/andrewjw/glowprom/commit/32d438c81028a12d305110d3e7dc672f49060113))

### Chores

- Update setup.py to allow installing from a source bundle, and only build the sdist package.
  ([`fde0a0b`](https://github.com/andrewjw/glowprom/commit/fde0a0bf99227f1da4c1283e87968f40d56d92b4))

### Features

- Install a local .tar.gz in docker to allow testing and more reliable releases.
  ([`380a5ff`](https://github.com/andrewjw/glowprom/commit/380a5ffd6671e8317ffde09093e4cefbec19f53b))


## v0.7.2 (2024-07-04)

### Bug Fixes

- Install rust compiler non-interactively.
  ([`2fc3f77`](https://github.com/andrewjw/glowprom/commit/2fc3f774c48feb5a7e3b619e9152ec3cbfcdef42))


## v0.7.1 (2024-07-04)

### Bug Fixes

- Install rust compiler in Docker to allow Python dependencies to build on arm v7.
  ([`6607555`](https://github.com/andrewjw/glowprom/commit/6607555e415bca7ef8c276cd265eab1a7e82ce41))


## v0.7.0 (2024-07-04)

### Features

- Build an arm v7 docker image for Raspberry Pi 3.
  ([`9dd06b9`](https://github.com/andrewjw/glowprom/commit/9dd06b9cf6c92ef2799ced64ed5b4ed1565b29b8))


## v0.6.4 (2024-07-03)

### Bug Fixes

- Fix docker build.
  ([`57277d1`](https://github.com/andrewjw/glowprom/commit/57277d152cf52c20d54ea26c30ea473d050b0293))


## v0.6.3 (2024-07-03)

### Bug Fixes

- Fix docker build.
  ([`6a38ae4`](https://github.com/andrewjw/glowprom/commit/6a38ae423469222c138b8342248da202f34b1790))


## v0.6.2 (2024-07-03)

### Bug Fixes

- Fix docker build.
  ([`3f4be5f`](https://github.com/andrewjw/glowprom/commit/3f4be5ff73a2f440eddb6495b8e3f429491c4356))


## v0.6.1 (2024-07-03)

### Bug Fixes

- Fix docker build.
  ([`ef92c79`](https://github.com/andrewjw/glowprom/commit/ef92c79fbaf430afcf45a2ce71549e8261588432))


## v0.6.0 (2024-07-03)

### Features

- Build both amd64 and arm64 images, and push both latest and tag versions.
  ([`78948de`](https://github.com/andrewjw/glowprom/commit/78948dedf0fdb0616a80e6e565f91c5da71dac18))


## v0.5.2 (2024-06-28)

### Bug Fixes

- Fix handling connection failure to MQTT broker. Get to 100% test coverage.
  ([`e8cac43`](https://github.com/andrewjw/glowprom/commit/e8cac43aa2fe9ada1de8a6e0cb79e9c7e482aefb))


## v0.5.1 (2024-06-28)

### Bug Fixes

- Fix tests.
  ([`ab5e0f0`](https://github.com/andrewjw/glowprom/commit/ab5e0f01c24e433289eab1ace088b48c1aa0a5d9))

- Upgrade to support paho-mqtt>=2.0.0.
  ([`16e4b1f`](https://github.com/andrewjw/glowprom/commit/16e4b1fd4f1bef1b6edcdab9d9107b6332e02cdc))


## v0.5.0 (2023-11-15)

### Chores

- Add some more badges to the readme.
  ([`87ba2cc`](https://github.com/andrewjw/glowprom/commit/87ba2cc020dc4939236fdf0fbb3984964663dd23))

- Add workflow badge.
  ([`53aa410`](https://github.com/andrewjw/glowprom/commit/53aa410922cf0e16cde6b66dcdd35b080b97a329))

- Don't automerge dockerfile changes, as they aren't tested.
  ([`f829460`](https://github.com/andrewjw/glowprom/commit/f8294602171c3a4bbce9d4c37cc9fd5810de36ce))

- Enable automerge for all dependency updates apart from major releases.
  ([`a1222d5`](https://github.com/andrewjw/glowprom/commit/a1222d578c9106acb2d7dbfe8003a9e060004355))

- Fix badge link
  ([`5d77b4c`](https://github.com/andrewjw/glowprom/commit/5d77b4cedeb2895c3c2a4e08ff76c7077b2d629e))

- Fix copy and paste errors
  ([`014982c`](https://github.com/andrewjw/glowprom/commit/014982c168837e55e73af0e9c6c8ad7612728299))

- Fix test if need to release.
  ([`3cd61f5`](https://github.com/andrewjw/glowprom/commit/3cd61f5b230b73492b5cb924588c0cd417fde574))

- Run action on pull requests.
  ([`ef464cd`](https://github.com/andrewjw/glowprom/commit/ef464cd8e25fc0d71a1b95b2e1cc24f788a6e105))

- Switch to coveralls as that supports newer coverage version. (fix #6)
  ([`237e98e`](https://github.com/andrewjw/glowprom/commit/237e98ea82d298758a69ec2d88b33963d3cf07e9))

- Test on Python 3.12
  ([`1d32e98`](https://github.com/andrewjw/glowprom/commit/1d32e9849244be8010d45a40712281df7f3e0168))

- Update action for semantic-release v8. ([#33](https://github.com/andrewjw/glowprom/pull/33),
  [`fb5bea6`](https://github.com/andrewjw/glowprom/commit/fb5bea69b297812881bcc21462267ee0135aa01d))

### Features

- Support Python 3.12 ([#44](https://github.com/andrewjw/glowprom/pull/44),
  [`04ad7ca`](https://github.com/andrewjw/glowprom/commit/04ad7ca6a833a32bc3819386f58b26721ffb9298))


## v0.4.5 (2023-03-27)

### Bug Fixes

- Fix typo.
  ([`00a0c16`](https://github.com/andrewjw/glowprom/commit/00a0c162cb9ab4bb9e69f970db337321b0049ca7))

- Set GH_TOKEN to allow GitHub releases to be updated.
  ([`f77f385`](https://github.com/andrewjw/glowprom/commit/f77f385058e920038fafa9575fc01fc87fc47d66))

### Chores

- Update action according to semantic release recommendations.
  ([`60d3783`](https://github.com/andrewjw/glowprom/commit/60d3783f2a3239ca8d41b3003352d0d89799e3d2))


## v0.4.4 (2023-03-23)

### Bug Fixes

- Build docker image as part of release process.
  ([`c3cc0e7`](https://github.com/andrewjw/glowprom/commit/c3cc0e7c3368344620f2c090aaa0d24f285bdc50))

- Maybe we don't need to install docker?
  ([`c28cb8a`](https://github.com/andrewjw/glowprom/commit/c28cb8aeefae43d83092ed591e11b54e10c057da))

- Typo.
  ([`e90a5dd`](https://github.com/andrewjw/glowprom/commit/e90a5ddb865db1df06551cca07435f33ba0a4e63))

- Use string not equals to test if we're releasing.
  ([`2b44f0c`](https://github.com/andrewjw/glowprom/commit/2b44f0c90b1ffc50a412d98892e842f3e5ae464f))


## v0.4.3 (2023-03-11)

### Bug Fixes

- Try to trigger on tags.
  ([`4269999`](https://github.com/andrewjw/glowprom/commit/426999952f33c64fed90925184cd8f70af132429))


## v0.4.2 (2023-03-11)

### Bug Fixes

- Install packaging to allow submission to PyPI
  ([`9960865`](https://github.com/andrewjw/glowprom/commit/9960865857ff10f54ca2023b8cb642cb9ab2de11))


## v0.4.1 (2023-03-11)

### Bug Fixes

- Set up git for release.
  ([`811d7e3`](https://github.com/andrewjw/glowprom/commit/811d7e3339eef718382675685aa28cce314bd07a))

### Chores

- Fix typo in action.
  ([`c035f7e`](https://github.com/andrewjw/glowprom/commit/c035f7e359f1314354af12245c1542b0b5407629))

- Fix typos.
  ([`a48cf52`](https://github.com/andrewjw/glowprom/commit/a48cf527163a9afb9975e49afb60672ac75744bb))

- Set up GitHub Actions to replace BuildBot. ([#22](https://github.com/andrewjw/glowprom/pull/22),
  [`2f56263`](https://github.com/andrewjw/glowprom/commit/2f5626371d5f096c3414afa7163a54b7f39ddd43))

- Try to fix secrets in Github action.
  ([`1c438f5`](https://github.com/andrewjw/glowprom/commit/1c438f524820a4dd9b19a3a1299d86126c40c19e))

### Features

- Check we can release through Actions.
  ([`63ef77c`](https://github.com/andrewjw/glowprom/commit/63ef77cf0cf8da1d12e60d100cff3ffeee2010a7))


## v0.4.0 (2023-03-10)

### Features

- Support multiple python versions.
  ([`648a85a`](https://github.com/andrewjw/glowprom/commit/648a85a5a72a6b068c9d1d5da19500591588c59e))


## v0.3.4 (2022-11-13)

### Bug Fixes

- Ignore 'read pending' messages.
  ([`312b129`](https://github.com/andrewjw/glowprom/commit/312b1291c748df4154e63961b54ba7cc61b842de))

### Chores

- Update readme to link to Docker Hub.
  ([`bdc044d`](https://github.com/andrewjw/glowprom/commit/bdc044d2e146172ec5443bf48d7b5ebcb67c712a))


## v0.3.3 (2022-11-09)

### Bug Fixes

- Handle exceptions when processing messages and keep running.
  ([`e4d1922`](https://github.com/andrewjw/glowprom/commit/e4d192209de4b7db8620ec6423a1f69cd8771974))


## v0.3.2 (2022-11-08)

### Bug Fixes

- Another fix for the docker image build.
  ([`b4fae0d`](https://github.com/andrewjw/glowprom/commit/b4fae0d717b8c2ca4153d4ad0562d58c4d1794bb))


## v0.3.1 (2022-11-08)

### Bug Fixes

- Fix pushing docker image.
  ([`4c86707`](https://github.com/andrewjw/glowprom/commit/4c8670793f00ada625332a6dc5d407f723e01abc))


## v0.3.0 (2022-11-08)

### Bug Fixes

- Reconnect if MQTT server is not available at start up.
  ([`128abcb`](https://github.com/andrewjw/glowprom/commit/128abcb78c7072b09ad246ca49bc398119ed513a))

### Chores

- Downgrade coverage and python-coveralls to fix reporting of code coverage.
  ([`dbee20b`](https://github.com/andrewjw/glowprom/commit/dbee20b2f58e354d4e67ab215b314b90c4c2bc40))

- Remove debug code.
  ([`00ea545`](https://github.com/andrewjw/glowprom/commit/00ea545b8356f414c95c2b21e4185f31bfd7942c))

- Replace coveralls library to support coverage >= 5.
  ([`78d9bd8`](https://github.com/andrewjw/glowprom/commit/78d9bd85ad6880f306b59b4d42d6d8f4a779e744))

### Features

- Add support for local MQTT servers.
  ([`1bb285c`](https://github.com/andrewjw/glowprom/commit/1bb285c9530df6c30d042765fdc45c7d3da7208b))


## v0.2.6 (2021-03-03)

### Bug Fixes

- Add Docker badge (mostly to test buildbot release)
  ([`f206b62`](https://github.com/andrewjw/glowprom/commit/f206b6209c0330ab8fff59ec0897099aacab497e))

- Fake commit to test release via buildbot.
  ([`633d588`](https://github.com/andrewjw/glowprom/commit/633d5888a67e9af3fd1fcdaeb4a55031590bd42c))

- Use python3 to build release package.
  ([`92f2070`](https://github.com/andrewjw/glowprom/commit/92f2070b4b0c2433c3fc1733dfa5121d8d93d980))

### Chores

- Add coveralls badge.
  ([`3304a73`](https://github.com/andrewjw/glowprom/commit/3304a73f1de06d6dbb887df5e27b66f1766e5b18))

- Fix coverage ignore for buildbot.
  ([`4d8b95c`](https://github.com/andrewjw/glowprom/commit/4d8b95c66daa739fc26579a4a0a2e39c8c2abb56))

- Push to docker if building a release tag.
  ([`3da59ed`](https://github.com/andrewjw/glowprom/commit/3da59ed8c3e13b62dc073586c1dd24b0fab3b7f7))

- Remove debug, and fix pip3 name.
  ([`c363cde`](https://github.com/andrewjw/glowprom/commit/c363cde5c9c7313065adbe1aaf73f10db493557f))

- Set coveralls token.
  ([`28f5e02`](https://github.com/andrewjw/glowprom/commit/28f5e02d61214c6578d4a93263adbf3ba09af803))


## v0.2.5 (2020-10-15)

### Bug Fixes

- Handle invalid messages, and print them for investigation.
  ([`e229b1e`](https://github.com/andrewjw/glowprom/commit/e229b1eaca70bcee6de23ab7d165e56849f9f0df))


## v0.2.4 (2020-10-14)

### Bug Fixes

- Add help and type for prometheus metrics.
  ([`dea4cd4`](https://github.com/andrewjw/glowprom/commit/dea4cd4310757ef564a0e4ec1ebf7ac4134a0364))

### Chores

- Fix code style.
  ([`721f055`](https://github.com/andrewjw/glowprom/commit/721f05585430f9db383d7d298f3abd8d97fffc55))


## v0.2.3 (2020-10-13)

### Bug Fixes

- Fix quotes in prometheus metrics.
  ([`6384617`](https://github.com/andrewjw/glowprom/commit/638461799bc71eb9d4496fbd76e978034acd6072))

### Chores

- Fix code style.
  ([`af494f5`](https://github.com/andrewjw/glowprom/commit/af494f55beb0f1e1f491bcb220524c61b3cd38d4))


## v0.2.2 (2020-10-13)

### Bug Fixes

- Fix prometheus style, removing initial blank line and simplifying formatting.
  ([`616c73f`](https://github.com/andrewjw/glowprom/commit/616c73f05e18789c0accc1c11e61a276ae7b1614))


## v0.2.1 (2020-10-09)

### Bug Fixes

- Fix typo when scaling monthly electricity consumption.
  ([`e69856d`](https://github.com/andrewjw/glowprom/commit/e69856ddcc6ce25079d7839798f8fd07c71acff9))

- Listen to mqtt on a separate thread so we can serve at the same time.
  ([`58a0bfb`](https://github.com/andrewjw/glowprom/commit/58a0bfbd4992e21bd23d564a367df524f68a68d2))


## v0.2.0 (2020-10-09)

### Features

- Convert data to prometheus metrics and serve over http.
  ([`0f2a5bd`](https://github.com/andrewjw/glowprom/commit/0f2a5bd3c73ae031e0abeec0fcd2ab73bced84b1))


## v0.1.1 (2020-10-01)

### Bug Fixes

- Fix typo in setup.py
  ([`4801d08`](https://github.com/andrewjw/glowprom/commit/4801d08b4c26776155e574ded1d464b724e8eb83))


## v0.1.0 (2020-09-30)

### Features

- Factor out connecting to MQTT and add tests.
  ([`6e59696`](https://github.com/andrewjw/glowprom/commit/6e59696bd0fd096e90c3551e929f89d844543907))


## v0.0.2 (2020-09-27)

- Initial Release

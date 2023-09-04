## Instalar Node 18

### Para windows

https://nodejs.org/dist/v18.17.1/node-v18.17.1-x64.msi

### Para Linux

wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash

En la consola tirar

```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" # This loads nvm
```

## Instalar

En la consola:

```bash
git clone https://github.com/ltisera/tpSD1.git
cd tpSD1
npm install
```

## Para levantar el front

```bash
npm run dev
```

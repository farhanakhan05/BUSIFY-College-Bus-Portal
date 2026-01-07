/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_KEY_BUSIFY: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

declare const process: {
  env: {
    [key: string]: string | undefined
  }
}


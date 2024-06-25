export const env = import.meta.env

export const isDevMode = env.CURRENT_ENV === 'dev'
export const isTestMode = env.CURRENT_ENV === 'test'
export const isProMode = env.CURRENT_ENV === 'pro'

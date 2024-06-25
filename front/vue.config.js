const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    resolve: {
      alias: {
        '@': require('path').resolve(__dirname, 'src'),
      },
    },
  },
  assetsDir: './src/assets',
  devServer: {
    port: 8080,
    // open: true,
  },
  publicPath: '/',
  outputDir: 'dist',
})

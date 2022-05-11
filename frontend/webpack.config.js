const path = require('path');
const webpack = require('webpack');

const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const BundleTracker = require('webpack-bundle-tracker');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const TerserPlugin = require("terser-webpack-plugin");
const { VueLoaderPlugin } = require('vue-loader');

const devMode = process.env.NODE_ENV !== 'production';
const hotReload = process.env.HOT_RELOAD === '1';

const vueRule = {
  test: /\.vue$/,
  loader: 'vue-loader',
  options: {
    reactivityTransform: true
  },
  exclude: /node_modules/
};

const styleRule = {
  test: /\.(sa|sc|c)ss$/,
  use: [
    MiniCssExtractPlugin.loader,
    { loader: 'css-loader', options: { sourceMap: true } },
    { loader: 'postcss-loader' },
    'sass-loader'
  ]
};

const jsRule = {
  test: /\.js$/,
  loader: 'babel-loader',
  include: path.resolve('./src'),
  exclude: /node_modules/
};

const assetRule = {
  test: /.(jpg|png|woff(2)?|eot|ttf|svg)$/,
  type: 'asset/resource'
};

const plugins = [
  new BundleTracker({ filename: './webpack-stats.json' }),
  new VueLoaderPlugin(),
  new MiniCssExtractPlugin({
    filename: devMode ? '[name].css' : '[name].[fullhash].css',
    chunkFilename: devMode ? '[id].css' : '[id].[fullhash].css'
  }),
  new BundleAnalyzerPlugin({ analyzerMode: 'static', openAnalyzer: false }),
  new webpack.HotModuleReplacementPlugin(),
  new CleanWebpackPlugin(),
  new CopyWebpackPlugin({
    patterns: [
      {
        from: 'static/**/*',
        to: path.resolve('./dist/[name][ext]'),
        toType: 'template'
      }
    ]
  })
];

if (devMode) {
  styleRule.use = ['css-hot-loader', ...styleRule.use];
} else {
  plugins.push(
    new webpack.EnvironmentPlugin(['NODE_ENV', 'SOURCE_VERSION'])
  );
}

module.exports = {
  context: __dirname,
  entry: './src/main.js',
  output: {
    path: path.resolve('./dist/'),
    filename: '[name]-[fullhash].js',
    publicPath: hotReload ? 'http://localhost:8080/' : ''
  },
  devtool: 'source-map',
  devServer: {
    hot: true,
    headers: { 'Access-Control-Allow-Origin': '*' }
  },
  module: { rules: [vueRule, jsRule, styleRule, assetRule] },
  plugins,
  optimization: {
    minimizer: [
      new TerserPlugin(),
      new OptimizeCSSAssetsPlugin({})
    ],
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          chunks: 'initial',
        },
      }
    }
  },
};

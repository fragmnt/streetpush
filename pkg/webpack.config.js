const path = require('path');
const HtmlWebPackPlugin = require('html-webpack-plugin');

module.exports = {
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'bundle.js',
  },
  resolve: {
    modules: [path.join(__dirname, 'src'), 'node_modules'],
    alias: {
      react: path.join(__dirname, 'node_modules', 'react'),
      public: path.join(__dirname, './public')
    },
  },
  module: {
    rules: [
      /* {
        test: /\.ttf$/,
        use: [
          {
            loader: 'ttf-loader',
            options: {
              name: '[hash].[ext]',
            },
          },
        ]
      }, */
      {
        test: /\.(jpe?g|png|gif|svg|woff|ttf|woff2)$/i,
        use: [
          'url-loader', // ?limit=25000
          'img-loader',
          'file-loader',
        ]
      },
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/,
        use: [
          {
            loader: 'style-loader',
          },
          {
            loader: 'css-loader',
          },
        ],
      },
    ],
  },
  plugins: [
    new HtmlWebPackPlugin({
      template: './public/index.html',
    }),
  ],
};
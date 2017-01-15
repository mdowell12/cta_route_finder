var path = require('path');

module.exports = {
    devtool: 'inline-source-map',
    entry: {
        app: "./public/js/app.js"
    },
    resolve: {
        root: [path.resolve(__dirname, "node_modules"), path.resolve(__dirname, "public/js")],
        extensions: ['', '.js', '.jsx']
    },
    output: {
        path: "public/dist",
        filename: "[name].js"
    },
    module: {
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015'],
                    plugins: ['syntax-jsx']
                }
            }
        ],
        exclude: /node_modules/,
        resolve: {
          extensions: ['.js', '.jsx']
        }
    }
}
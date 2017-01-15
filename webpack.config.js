// module.exports = {
//      devtool: "#inline-source-map",
//      entry: {
//         javascript: "./public/js/app.js",
//         html: './public/templates/index.html'
//      },
//      output: {
//          path: './public/dist',
//          filename: 'app.bundle.js',
//      },
//     resolve: {
//       extensions: ['', '.js', '.jsx', '.json']
//     },
//     module: {
//       loaders: [
//         {
//           test: /\.jsx?$/,
//           exclude: /node_modules/,
//           loaders: ["babel-loader"]
//         },
// 	{
//           test: /\.html$/,
//           loader: "file?name=[name].[ext]",
//         }
//       ]
//     }
// }


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
        path: "./public/dist",
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
                    // plugins: ['syntax-jsx', 'transform-h-jsx']
                }
            }
        ],
        exclude: /node_modules/,
        resolve: {
          extensions: ['.js', '.jsx']
        }
    }
}
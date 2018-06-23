var path = require('path');

module.exports = {
    entry: './index.js',
    output: {
        filename: 'impakt.js',
        path: path.resolve(__dirname, 'impakt/static/js/')
    },
    module:{
        rules: [{
            test: /\.scss$/,
            use: [
                "style-loader", //creates styles from JS strings
                "css-loader", // css to JS
                "sass-loader", // scss to CSS
            ]
        }]
    }
}

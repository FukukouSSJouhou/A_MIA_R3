import path from 'path';
import * as wdevpack from 'webpack-dev-server';
import { Configuration } from 'webpack';
import  HtmlWebpackPlugin from 'html-webpack-plugin';
import CopyWebpackPlugin from 'copy-webpack-plugin';
const isDev = process.env.NODE_ENV === 'development';
const isReactOnly=process.env.REACT_DEVENV==="devreactonly"
const common:Configuration={
    mode: isDev ? 'development' : 'production',

    resolve: {
        extensions: ['.js', '.jsx','.json', '.ts', '.tsx','.node']
    },
    
    output: {
        path: path.resolve(__dirname, 'build'),
        filename: '[name].js'
    },
    module: {
        rules: [
            {
                test: /\.tsx?$/,
                use: "ts-loader",
                include: path.resolve(__dirname, 'src'),
                exclude: /node_modules/
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
              test: /\.node$/,
              loader: "node-loader",
            },
        ]
    },
    watch: isDev,
    devtool: isDev ? 'inline-source-map' : undefined,
}
const main:Configuration={
    ...common,
    target:"electron-main",
    entry:{
        main:"./src_electron/electron.ts"
    },
    output:{
        path: path.resolve(__dirname, 'build'),
        filename: 'electron.js'
    },

};
const preload:Configuration={
    ...common,
    target:"electron-preload",
    entry:{
        preload:"./src_electron/preload.ts"
    }
}
const renderer:Configuration={
    ...common,
    target:"web",
    
    entry: "./src_node/index.tsx",
    output:{
        path: path.resolve(__dirname, 'build'),
        filename: 'index.js'
    },
    devServer: {
        port: 3000,
        historyApiFallback: true,
        static: { directory: path.join(__dirname, 'public'), }
    },
    
    plugins: [
        new HtmlWebpackPlugin({
            template: './src_node/index.html',
        }),
        new CopyWebpackPlugin(
            {
                patterns:[
                    {from:"public",to:"./"}
                ]
            }
        )
    ],

};
const config=isDev?[renderer]:[main,preload,renderer];
export default config;
/*
module.exports = {
    mode: "development",
    entry: "./src_node/index.tsx",
    output: {
        path: path.resolve(__dirname, 'build'),
        filename: "index.js"
    },
    devtool: 'source-map',
    devServer: {
        port: 3000,
        historyApiFallback: true,
        static: { directory: path.join(__dirname, 'public'), }
    },
    plugins: [
        new HtmlWebpackPlugin({
            template: './src_node/index.html',
        }),
        new CopyWebpackPlugin(
            {
                patterns:[
                    {from:"public",to:"./"}
                ]
            }
        )
    ],
}*/
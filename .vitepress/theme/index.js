// .vitepress/theme/index.js

import DefaultTheme from 'vitepress/theme-without-fonts'; //不使用默认字体
import 'lxgw-wenkai-screen-web/style.css'; // 导入霞鹜文楷屏幕阅读版
import 'noto-sans-sc/all.css'; // 导入 noto，思源宋体加粗后辨识度不高
import './custom.css';
import Layout from './Layout.vue';


export default {
  ...DefaultTheme,
  Layout,
};

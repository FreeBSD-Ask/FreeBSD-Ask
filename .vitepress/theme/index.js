// .vitepress/theme/index.js

import DefaultTheme from 'vitepress/theme-without-fonts'; //不使用默认字体
import 'lxgw-wenkai-screen-web/style.css'; // 导入霞鹜文楷屏幕阅读版
import '@wc1font/source-han-serif-sc-vf/font.css'; // 导入思源宋体
import './custom.css';
import Layout from './Layout.vue';


export default {
  ...DefaultTheme,
  Layout,
};

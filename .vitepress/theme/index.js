// .vitepress/theme/index.js

import DefaultTheme from 'vitepress/theme-without-fonts'; //不使用默认字体
import './custom.css';
import Layout from './Layout.vue';
import 'lxgw-wenkai-gb-web/style.css';


export default {
  ...DefaultTheme,
  Layout,
};

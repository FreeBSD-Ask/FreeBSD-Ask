// .vitepress/theme/index.js

import DefaultTheme from 'vitepress/theme-without-fonts'; //不使用默认字体
import 'lxgw-wenkai-screen-web/lxgwwenkaigbscreen/result.css'; // 导入霞鹜文楷屏幕阅读版
import 'lxgw-wenkai-screen-web/lxgwwenkaimonogbscreen/result.css'; // 导入霞鹜文楷屏幕阅读版
import 'noto-sans-sc/all.css'; // 导入 noto，思源宋体加粗后辨识度不高
import './custom.css'; //导入自定义 CSS 样式
import Layout from './Layout.vue'; // 导入评论插件和图片缩放插件
import { h } from 'vue';  // 评论插件需要

export default {
  ...DefaultTheme,
  Layout,
};

import {
	defineConfig
} from 'vitepress';
import autoNav from "vite-plugin-vitepress-auto-nav";
import footnote from 'markdown-it-footnote';
import mathjax3 from 'markdown-it-mathjax3-tao';
import taskLists from 'markdown-it-task-checkbox';
import {
	chineseSearchOptimize,
	pagefindPlugin
} from 'vitepress-plugin-pagefind';
import {
	defineConfig
} from 'vitepress';

const customElements = [
	'mjx-container',
	'mjx-assistive-mml',
	'math',
	'maction',
	'maligngroup',
	'malignmark',
	'menclose',
	'merror',
	'mfenced',
	'mfrac',
	'mi',
	'mlongdiv',
	'mmultiscripts',
	'mn',
	'mo',
	'mover',
	'mpadded',
	'mphantom',
	'mroot',
	'mrow',
	'ms',
	'mscarries',
	'mscarry',
	'mscarries',
	'msgroup',
	'mstack',
	'mlongdiv',
	'msline',
	'mstack',
	'mspace',
	'msqrt',
	'msrow',
	'mstack',
	'mstack',
	'mstyle',
	'msub',
	'msup',
	'msubsup',
	'mtable',
	'mtd',
	'mtext',
	'mtr',
	'munder',
	'munderover',
	'semantics',
	'math',
	'mi',
	'mn',
	'mo',
	'ms',
	'mspace',
	'mtext',
	'menclose',
	'merror',
	'mfenced',
	'mfrac',
	'mpadded',
	'mphantom',
	'mroot',
	'mrow',
	'msqrt',
	'mstyle',
	'mmultiscripts',
	'mover',
	'mprescripts',
	'msub',
	'msubsup',
	'msup',
	'munder',
	'munderover',
	'none',
	'maligngroup',
	'malignmark',
	'mtable',
	'mtd',
	'mtr',
	'mlongdiv',
	'mscarries',
	'mscarry',
	'msgroup',
	'msline',
	'msrow',
	'mstack',
	'maction',
	'semantics',
	'annotation',
	'annotation-xml',
	'mjx-c',
	'mjx-mstyle',
	'mjx-mspace',
	'mjx-mover',
	'mjx-base',
	'mjx-over',
	'mjx-texatom',
	'mjx-mfrac',
	'mjx-frac',
	'mjx-dbox',
	'mjx-dtable',
	'mjx-row',
	'mjx-den',
	'mjx-dstrut',
	'mjx-line',
	'mjx-num',
	'mjx-mrow',
	'mjx-msqrt',
	'mjx-sqrt',
	'mjx-box',
	'mjx-surd',
	'mjx-nstrut',
	'mjx-msup',
	'mjx-script',
	'mjx-math',
	'mjx-mn',
	'mjx-mo',
	'mjx-mi',
];

export default defineConfig({
	sitemap: {
		hostname: 'https://docs.bsdcn.org',
	},
	lang: 'zh-CN',
	lastUpdated: true,
	title: "FreeBSD 艺术科学哲学导论",
	description: "FreeBSD 艺术科学哲学导论",
	metaChunk: true,
	markdown: {
		image: {
			lazyLoading: true
		},
		config(md) {
			md.use(footnote);
			md.use(mathjax3, {
				tex: {
					tags: 'ams'
				},
				loader: {
					load: ["input/tex", "output/chtml"]
				},
			});
			md.use(taskLists, {
				disabled: true,
				divWrap: false,
				divClass: 'checkbox',
				idPrefix: 'cbx_',
				ulClass: 'task-list',
				liClass: 'task-list-item',
			});
			md.renderer.rules.footnote_anchor = function render_footnote_anchor(tokens, idx, options, env, slf) {
				let id = slf.rules.footnote_anchor_name?.(tokens, idx, options, env, slf)
				if (tokens[idx].meta.subId > 0) {
					id += ':' + tokens[idx].meta.subId
				}
				return ' <a href="#fnref' + id + '" class="footnote-backref">🔼</a>'
			};
			const defaultCodeInline = md.renderer.rules.code_inline;

			md.renderer.rules.code_inline = (tokens, idx, options, env, self) => {
				tokens[idx].attrSet('v-pre', '');
				return defaultCodeInline(tokens, idx, options, env, self);
			};
		}

	},
	vue: {
		template: {
			compilerOptions: {
				isCustomElement: (tag) => customElements.includes(tag),
			},
		},
	},
	head: [
		[
			'script',
			{},
			`import('/pagefind/pagefind.js')
        .then((module) => {
          window.__pagefind__ = module
          module.init()
        })
        .catch(() => {
          // console.log('not load /pagefind/pagefind.js')
        })`
		],
		['link', {
			rel: 'icon',
			href: '/favicon.ico'
		}],
		['meta', {
			name: 'keywords',
			content: ''
		}],
		[
			'script',
			{
				async: '',
				src: 'https://cdn.bootcdn.net/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js',
			}
		],
		[
			'script',
			{
				async: '',
				src: 'https://www.googletagmanager.com/gtag/js?id=G-GKTJ5MJJ58'
			}
		],
		[
			'script',
			{},
			`window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-GKTJ5MJJ58');`
		],
	],
	rewrites: {
		'SUMMARY.md': 'index.md',
	},
	themeConfig: {
		siteTitle: 'FreeBSD 中文社区',
		langMenuLabel: '多语言',
		returnToTopLabel: '回到顶部',
		darkModeSwitchLabel: '主题',
		lightModeSwitchTitle: '切换到浅色模式',
		darkModeSwitchTitle: '切换到深色模式',
		docFooter: {
			prev: '上一页',
			next: '下一页'
		},

		logo: {
			src: '/logo.svg',
			width: 24,
			height: 24
		},
		nav: [
   {
    text: 'QQ 群 787969044',
    link: 'https://qm.qq.com/q/cX5mpJ36gg'
   },
			{
				text: 'FreeBSD 中文社区',
				link: 'https://bsdcn.org'
			},
			{
				text: '回到主站',
				link: 'https://book.bsdcn.org'
			},
			{
				text: '目录',
				link: 'mu-lu.md'
			},
			{
				text: '视频教程Ⅰ',
				link: 'https://www.bilibili.com/video/BV1Qji2YLEgS/'
			},
			{
				text: '视频教程Ⅱ',
				link: 'https://www.bilibili.com/video/BV12m4y1w7FS/'
			},

		],
		base: '/',
		editLink: {
			text: '在 GitHub 上编辑此页面',
			pattern: 'https://github.com/FreeBSD-Ask/FreeBSD-Ask/edit/main/:path'
		},
		outline: {
			label: '此页目录',
			level: 'deep'
		},
		sidebarMenuLabel: '目录',
		lastUpdated: {
			text: '最后更新于',
			formatOptions: {
				dateStyle: 'short',
				timeStyle: 'medium'
			}
		},
	},


	vite: {
		plugins: [pagefindPlugin({
				customSearchQuery: chineseSearchOptimize,
				btnPlaceholder: '搜索',
				placeholder: '搜索文档',
				emptyText: '空空如也',
				heading: '共: {{searchResult}} 条结果',
				excludeSelector: ['img', 'a.header-anchor'],
			}),
			autoNav({
				summary: {
					target: "docs/SUMMARY.md",
					collapsed: false,
				}
			})
		],
	},
})

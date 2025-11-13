<script setup lang="ts">
import DefaultTheme from "vitepress/theme";
import { onMounted, watch } from "vue";
import { useRouter, inBrowser, useData } from "vitepress";
import mediumZoom from "medium-zoom";
import Giscus from "@giscus/vue";

const { Layout } = DefaultTheme;
const router = useRouter();
const { isDark, page } = useData();

// Setup medium zoom with the desired options
const setupMediumZoom = () => {
  if (!inBrowser) return;
  mediumZoom("[data-zoomable]", {
    background: "transparent",
  });
};

// Apply medium zoom on load
onMounted(setupMediumZoom);

// Re-apply medium zoom on route changes
router.onAfterRouteChange = setupMediumZoom;

// Watch for dark mode changes to update Giscus theme
watch(isDark, (dark) => {
  if (!inBrowser) return;

  const iframe = document
    .querySelector("giscus-widget")
    ?.shadowRoot?.querySelector("iframe");

  iframe?.contentWindow?.postMessage(
    { giscus: { setConfig: { theme: dark ? "dark" : "light" } } },
    "https://giscus.app"
  );
});
</script>

<template>
  <Layout>
    <template #doc-footer-before> </template>
    <template #doc-after>
      <div style="margin-top: 24px">
        <Giscus
          :key="page.filePath"
          repo="FreeBSD-Ask/Handbook-giscus-discussions"
          repo-id="R_kgDOIFzFKw"
          category="General"
          category-id="DIC_kwDOIFzFK84CRsdz"
          mapping="pathname"
          strict="0"
          reactions-enabled="1"
          emit-metadata="0"
          input-position="bottom"
          lang="zh-CN"
          crossorigin="anonymous"
          :theme="isDark ? 'dark' : 'light'"
        />
      </div>
    </template>
  </Layout>
</template>

<style>
.medium-zoom-overlay {
  backdrop-filter: blur(5rem);
}

.medium-zoom-overlay,
.medium-zoom-image--opened {
  z-index: 999;
  scrollOffset: 9999;
}
</style>

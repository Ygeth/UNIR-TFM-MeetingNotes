<template>
  <v-app>
    <HeaderComponent />
    <v-main>
      <v-container>
        <SidebarComponent />
        <v-row>
          <v-col cols="8">
            <MainContentComponent />
          </v-col>
          <v-col cols="4">
            <VideoComponent />
          </v-col>
        </v-row>
        </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import HeaderComponent from './components/HeaderComponent.vue';
import SidebarComponent from './components/SidebarComponent.vue';
import MainContentComponent from './components/MainContentComponent.vue';
import VideoComponent from './components/VideoComponent.vue';

import reportService from '@/services/reportService';
// export default {
//   name: 'App',
//   components: {
//     HeaderComponent
//   }
// }
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
  margin-top: 60px;
}
</style>

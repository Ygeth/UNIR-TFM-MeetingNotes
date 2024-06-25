<template>
  <v-app-bar app>
    <v-toolbar-title>{{ state.title }}</v-toolbar-title>
    <v-spacer></v-spacer>
    <div>{{ state.date }}</div>
    <v-btn text>Recap</v-btn>
    <v-btn text>Deep Dive</v-btn>
    <v-btn text>Coaching</v-btn>
  </v-app-bar>
</template>

<script setup>
import { reactive } from 'vue';
const state = reactive({
  date: 'vie, 23 feb 2024 | 1:30-1:52 pm',
  title: 'Sprint planning - Mejoras de Prevención Técnica',
});
</script>

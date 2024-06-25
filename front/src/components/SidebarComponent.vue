<template>
  <v-navigation-drawer app permanent>
    <v-list dense>
      <!-- User Info Section -->
      <v-list-item>
        <v-list-item-avatar>
          <v-avatar color="primary" size="40">
            <v-icon dark>mdi-account-circle</v-icon>
          </v-avatar>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title>Ricardo Montaner</v-list-item-title>
          <v-list-item-subtitle>ricardo.montaner@sngular.com</v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <!-- Navigation Links -->
      <v-list-item link>
        <v-list-item-icon>
          <v-icon>mdi-file-document</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Reports</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link>
        <v-list-item-icon>
          <v-icon>mdi-coach-lamp</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Coaching</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link>
        <v-list-item-icon>
          <v-icon>mdi-lightbulb</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Recommendations</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-list-item link>
        <v-list-item-icon>
          <v-icon>mdi-calendar</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Calendar</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script setup>
import { reactive } from 'vue';
const state = reactive({
  date: 'vie, 23 feb 2024 | 1:30-1:52 pm',
  title: 'Sprint planning - Mejoras de Prevención Técnica',
});
</script>

<style scoped>
.v-list-item {
  transition: background-color 0.3s;
}

.v-list-item:hover {
  background-color: #f0f0f0;
}

.v-list-item-avatar .v-avatar {
  background-color: #1976D2;
}

.v-navigation-drawer {
  background-color: #FFFFFF;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
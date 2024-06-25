<template>
  <v-container v-for="(section, index) in state.sectionList" :key="index">
    <v-card class="pt-0">
      <v-card-title>{{ section.title }}</v-card-title>
      <v-card-text>
        {{ section.content }}
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script setup>
import { reactive } from 'vue';
const state = reactive({
  date: 'vie, 23 feb 2024 | 1:30-1:52 pm',
  title: 'Sprint planning - Mejoras de Prevención Técnica',
  sectionList: [
    {
      title: 'Summary',
      content: 'Se discutieron varios temas relacionados con la finalización de proyectos, la necesidad de pruebas y problemas técnicos. Se abordaron problemas específicos, como la selección de centros en la plataforma y la presencia de duplicados en la base de datos. También se acordó comenzar la validación de pruebas la próxima semana y subir una versión en un mes. Se cerraron fechas de versión en el seguimiento del jueves siguiente.'
    },
    {
      title: 'Action Items',
      content: 'Se acordó comenzar la validación de pruebas la próxima semana y subir una versión en un mes. Se cerraron fechas de versión en el seguimiento del jueves siguiente.'
    },
    {
      title: 'Next Steps',
      content: 'Se cerraron fechas de versión en el seguimiento del jueves siguiente.'
    }
  ]
});
</script>
<style scoped>
.v-card {
  transition: box-shadow 0.3s;
}

.v-card:hover {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

.v-card-title {
  font-weight: bold;
}
</style>
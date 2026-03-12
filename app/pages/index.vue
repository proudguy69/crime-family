<template>
    <UHeader title="Famiglia Sangue">

        <UNavigationMenu :items="items" />

        <template #right>
            <UButton to="/authorize">Login</UButton>
        </template>
    </UHeader>
</template>

<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui';


const items = ref<NavigationMenuItem[]>([
    {
        label: "yourmom"
    }
])

</script>
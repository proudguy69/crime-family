<template>
    <UHeader title="Famiglia Sangue">

        <UNavigationMenu :items="items" />

        <template #right>
            <UButton v-if="!user_information.discord_id" :to="discord_auth">Discord Login</UButton>
            <UButton v-else>{{ user_information.discord_username }}</UButton>
        </template>
    </UHeader>
</template>

<script setup lang="ts">
import type { NavigationMenuItem } from '@nuxt/ui';

// varibles
const items = ref<NavigationMenuItem[]>([

])

// injects
const discord_auth = inject("discord_auth")!
const user_information = inject<Ref>("user_information")!


</script>
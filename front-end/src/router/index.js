import Vue from 'vue'
import Router from 'vue-router'
import Ping from '@/components/Ping'
import Expense from '@/components/Expense'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'Ping',
            component: Ping
        },
        {
            path: '/expense',
            name: 'expense',
            component: Expense,
        },

    ]
})

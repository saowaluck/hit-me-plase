describe('Landing Page', () => {
    it('Should be able to submit form with email', () => {
        const user = cy
        user.visit('http://localhost:8000')
        user.get('h1')
            .contains('Hit Me!')
        user.get('input[name="email"]')
            .type('pop@prontomarketing.com')
        user.get('button[type="submit"]')
            .click()

        const admin = cy
        admin.visit('http://localhost:8000/admin/')
        admin.get('input[name="username"]')
            .type('admin')
            .get('input[name="password"]')
            .type('Pronto123')
            .get('button[type="submit"]')
            .click()
        admin.get('xyz')
            .click()
            .get('abc')
            .click()
            .contains('pop@prontomarketing.com')
    })
})

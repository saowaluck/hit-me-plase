describe('Landing Page', () => {
    it('Should be able to submit form with email', () => {
        const user = cy
        user.visit('http://localhost:8000')
        user.get('h1')
            .contains('Hit Me please!')
        user.get('input[name="email"]')
            .type('pop@prontomarketing.com')
        user.get('input[type="submit"]')
            .click()

        const admin = cy
        admin.visit('http://localhost:8000/admin/')
        admin.get('input[name="username"]')
            .type('pop')
            .get('input[name="password"]')
            .type('Pronto123')
            .get('input[type="submit"]')
            .click()
        admin.get('.model-hitter > th > a')
            .click()
        admin.get('.field-email > a').should('contain', 'pop@prontomarketing.com')
    })
})

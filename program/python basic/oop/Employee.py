class Employee:
    def calc_allowance(self, bp):
        """Example allowances: HRA 10% + DA 5% of basic pay."""
        return (bp * 0.10) + (bp * 0.05)

    def calc_ded(self, bp):
        """Example deduction: 8.3% of basic pay (PF/other)."""
        return bp * 0.083

    def calc_grosspay(self, bp):
        """Gross = basic + allowances."""
        return bp + self.calc_allowance(bp)

    def calc_netpay(self, bp):
        """Net = gross - deductions."""
        gross = self.calc_grosspay(bp)
        deductions = self.calc_ded(bp)
        return gross - deductions
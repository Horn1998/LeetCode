#time 91 room 5
def computeArea(A, B, C, D, E, F, G, H):
        area1 = abs(D - B) * abs(A - C)
        area2 = abs(F - H) * abs(E - G)
        if C <= E or G <= A or D <= F or H <= B:
            return area1 + area2
        area3 = abs(min(H,D) - max(B,F)) * abs(min(C,G) - max(A,E))
        return area1 + area2 - area3
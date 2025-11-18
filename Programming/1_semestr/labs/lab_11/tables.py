def table_results(i1, i1_absolut, i1_relative, i2, i2_absolut, i2_relative, i3, i3_absolut, i3_relative, i4, i4_absolut, i4_relative, n1, n2):
    delimer = '-' * (16 + 58 * 2)
    print(delimer)
    print(f'|{" "*16}|{f"N1={n1:.6g}":^56}|{f"N2={n2:.6g}":^56}|')
    print(delimer)
    print(f'|{" " * 16}|{"integral":^18}|{"absolut":^18}|{"relative":^18}|{"integral":^18}|{"absolut":^18}|{"relative":^18}|')
    print(delimer)
    print(f'|{"Right rect":<16}|{i1:^18.6g}|{i1_absolut:^18.6g}|{f"{i1_relative:.6g}%":^18}|{
          i2:^18.6g}|{i2_absolut:^18.6g}|{f"{i2_relative:.6g}%":^18}|')
    print(delimer)
    print(f'|{"Simpson":<16}|{i3:^18.6g}|{i3_absolut:^18.6g}|{f"{i3_relative:.6g}%":^18}|{
          i4:^18.6g}|{i4_absolut:^18.6g}|{f"{i4_relative:.6g}%":^18}|')
    print(delimer)

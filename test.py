import means
cs111x_enrollments = [[614, 88, 144],
                      [534, 59, 148],
                      [0, 0, 0],
                      [682, 77, 146],
                      [501, 93, 136],
                      [44, 0, 0]]

print(means.mean_by_row(cs111x_enrollments))
print(means.mean_by_col(cs111x_enrollments))
print(means.mean_all(cs111x_enrollments))
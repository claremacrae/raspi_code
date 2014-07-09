Graphics[Rectangle[{10, 10}, {20, 20}]]
Graphics[Rectangle[]]
Graphics[{Red, Rectangle[{0, 0}],
          Blue, Rectangle[{0.5, 0.5}]}]
Show[Graphics[Rectangle[{0, 0}, {16, 20}]], Axes -> True, 
AxesStyle -> Black]
 
Graphics[{Gray, Rectangle[{0, 0}, {20, 16}]}]

Graphics[{Gray,
  Rectangle[{0, 0}, {20, 16}],
  Rectangle[{0 + 25, 0}, {20 + 25, 16}]}
  ]


 
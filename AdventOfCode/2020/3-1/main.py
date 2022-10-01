input = [
"....#............#.###...#.#.#.",
".#.#....##.........#.....##.#..",
".#..#.#...####.##..#......#..##",
"......#...#...#.......#........",
"........#...###..#.#....#....#.",
"..##.....#.....#.#.........#.#.",
".##.......#.#.#...#..#...##...#",
"...##.....#....##....#...###.#.",
"..#...#......##.#.##.....#.#..#",
".#....#.###.........#..........",
".#.#..##.....###.....###....#.#",
"....###....#......#...#......##",
"......##...#.##.........#.#..#.",
"##.#....##...#..##....#.#..#.##",
".#...#..#.....#.#.......#...#..",
"..........#..###.###......##..#",
"..#.##.#..#......#.......###.#.",
"...#...#.#.#..#...#.#..........",
"#........#..#..#.#....#.##..###",
"#...#.....#..####.........####.",
".....###..........#.#...##...#.",
".....#...#..#.......#....##.#..",
"...........#..##.....#...#..#..",
"......##..#........#...........",
"#.#..#.#.#..#.....#....#.....#.",
"..#....##....##...#.....#......",
".#.#....#..#.#......#..###...#.",
".......#...#.#....##..#..#..#..",
".#.#.#.......#....#.#.#.......#",
".#..........#.##.#...#..#.#.##.",
"..#.#..........#.#....##.#.##..",
"###..#..#.#...##.#.#..#........",
"##....#...#....#....#...#.#....",
"#...#.#....#.##..##...#.#......",
"......#...#.###......##....#...",
".................#.###......#..",
"##..#....#....##...###.#.#..###",
"..#..........#..####..##..#...#",
".#......#..#.#...........##.#..",
".#..#......#...#.#.#..#.#.#.#.#",
".#......###.....#.#.#......##..",
"#..........#.##...#...........#",
"..#....#.##....#.........#.....",
".#..##....#...##.........#..#..",
"....##..#.###..#.#...#..###..#.",
"..#......#........#...#.#......",
"........#..#..#..#...#.##......",
".##.#.#......#...#.........#...",
"#..###.#...#....###.##..###....",
"........##.............#....#..",
"...#...............#....#.#....",
"#..........#..#..#.#.....#...#.",
".#.............#...#.......#..#",
".#..#..#...#........##.........",
".....#.#..#.#..#..##.........#.",
"..#..##...#....#.#...#.###..#..",
"#...........##.....#...#.##....",
"#.#.#.#........##......#...#.#.",
"......#..#.###.#...#.##.##....#",
".#....#...#....#........#....#.",
"..#.#..........#..##.......#..#",
".....#...##..#................#",
".#...............##...#.##...##",
"#.####....##.....#.......#.##..",
"......#.##.#...##..###..#.#....",
".#.##.#...##..#.......#.#..#...",
"#...#.##..........##..........#",
"#.###...#...#..#.....#.#.##..##",
".##.....#....#...##.....##.....",
"...#........#..###.###...#.....",
"##..#....#.....#...#.#....#.#..",
"#....#....#.#..........#...#..#",
"...##..#......#..#..#..#..#....",
".....##...#..####..##.........#",
".....#..#.#...#..#....##..##...",
"..#.......##.#..#.##...#.#....#",
".#..#.#...##..##....#..#......#",
"..##.##..##...###..#....#...#..",
"........##.......##...##.....##",
".#....###...#..#..#..#.......#.",
"#.###............#....##.....#.",
"..........#...#...##..#...#....",
"..#......#.##.......#....##..##",
"..#..###.....#...#.......#.....",
"#.#...##.....#...#....#.......#",
"....##.##.#....#.....#.#....#..",
"...#....#.###............#..###",
"#..##..#.........##.....#.#...#",
"....#.......##......#....#...#.",
"....#..##.#..........#.........",
"....#...#.###.......#...#.#....",
"#..#..#...#.......##...#..#.##.",
"#.......#...##.##......#.......",
"##..##...##...#......#...#...##",
"..#...#.#.####.#...##.....##...",
"#...#..#..#...##......#.#..#..#",
"..##..##.#.#..#...####.....###.",
".#........#..##.###...#.##.#...",
"........#..#...##......#.#....#",
"..#...###.......##..##..#....#.",
".##...#.#..#.##.......##.###...",
"#....#.#.#........#....#..#.##.",
"....#.##.#.##..#.#####.....###.",
"#.#..#..#...#.#..#.......#.#...",
"....#...#....###...............",
".###.#.....#.#.......###......#",
"##...#.#.###....##..#...##.....",
"...#.#..#.###.#.......#...#.#..",
".#...#....#...#..####....###...",
"..#....##.....##.#.#.##....#...",
"#....#..##.......#...##.##....#",
".##..#.......#..#....###.......",
"#.##.....##.#.........#......##",
".####.#...#.....#..#...#.##..#.",
"....#...........#.....#........",
".#............##...#.......#.#.",
"#....#.##........#....#.#..#..#",
"#....#.##....#...##...#..#..#..",
"...#..#.####.#....#............",
"....#......#.........#.........",
"#....##....###.....#......#.#..",
"...#..#....#........###..#...#.",
"..#.#........#.#.#.###..#.#.#..",
".....###.....##.#....###.#.....",
"##.#....#....##...##.###.#.##..",
".###.#..#.......##...#...##....",
".#...###........#.......##.##..",
"#......####...#...##.#.######..",
"....##.............#..##.##...#",
"...........#..##.#...#.#.#...#.",
"###.......#.##..#....#...#....#",
".........#.....#.#.#..##.#.....",
"#...##..#....#..#.............#",
"...#.......#.##.............#.#",
".....#..#...##......####..#....",
".#.#.#.....#...####..#...##...#",
"#...#.#..#..#.#..#.##..........",
".....#.##..#.#.##..#.#.#....#.#",
"...##..#...#...#..#....#.......",
"........#.#..#...#...#.#...#...",
"##..#........#..#.....#......##",
".........#..#...#......#......#",
"..#.#.#........##...#.##.....##",
".###....##....#...#....#..#....",
".#.............###...#..##..###",
".##.##.##.......###.........#.#",
"..#..###...#...#....#..#.#..#.#",
"......#..#.#..#.....#.#........",
"......#...####...#.#.....#.....",
".#...##.......#..#......#...#..",
"#..#...#.......###..#..#.#.#.#.",
".....#.....###.##....#.#.##.#.#",
"#........#....##...#..#.##..#..",
"...#.#........##....#.#..###.#.",
"#...#...##.........#........###",
"##...#.##..##...#.....#.###.#..",
"#.###.#.#..#...........##..#...",
"........#.......#..#..#.###....",
"#........#....#......###.......",
"..#.###.######...#.###..#......",
"...#...######..#.....#....#.#..",
"..#.......#..#..#.........#...#",
".#...#..##.##.........##.......",
".........#.#.##.#..#....#.#...#",
"#.......#....#......#.....###.#",
"##..............#.###........#.",
"..#.##..#.##.....#...#.#.#..###",
"..#.#......#..#..##.#........#.",
"..#.....#...#.#...#...###..#.#.",
".......#...........#..#..#.#.##",
".......#...##..#.###...........",
".#........#.###.#..#..#..#..#..",
"##.#.##....#..###..#.##.##...#.",
".....#....##.#........#.#.#....",
"....##....#..#..#....##....#.#.",
"#.....##....#.....#.###.#....#.",
".#.##.##..#..#...#...........##",
"...#..###..#.....##....#.......",
"...#..##..###.#..#..#.#........",
"......##..#.......#..##.....###",
".#...##.#.#.#......#...#.#.#.##",
"....#.#....#...#........#...#..",
"....#.#......#.#.###.#.#.##.#..",
"#..#........###..#..#..#.....#.",
"...#....#...##...#........##.##",
".....#..#..#.....#....#.#...#..",
"..#.###....#.#..##......#.##.#.",
"..####......#..#.#.#..#.#####..",
".......##..#..###.#............",
"..###.#........#..........##.##",
"#.#.........#.##.#......#..#...",
"...#.....#.....##..#..##.##..#.",
"#.#.##....#.......###....##....",
"...##.#..#...##.#..#......#..#.",
"..##.........#.##.#####...#.#..",
".#....#...#....#.#.....##...###",
"##.....#..####............###.#",
"......#...........#....#.......",
".#......#.....##...........###.",
"#......##.......#.#.#..##.....#",
"...###.#.....##.#...#.#....#.#.",
"...###.......#...#.............",
"..#..#.#....#.#.###.#.#.##..##.",
"..##...#..#.#..##.#.##....##...",
"..#...........#..#....#....#...",
"#.##...........#..#.#..##.#.#..",
"...##...##................#..#.",
".#...#.##......#.#......#.####.",
"#.##....#....#.........#....###",
".....###........#.#.#.##...#.##",
".....#....#.#....#.........#..#",
"..#...#.#.#.#...#...#...##.#..#",
"###.......#.....#.............#",
"#.####.#.......#.#.#.#..#.#....",
"#..#..#####......#....#..##....",
"...............#.....#.#....###",
".###.....#...#.##..#.#..#.#####",
"#.##.....#......##.......##....",
"..........###.......#...#.#....",
"..#.#..#...##.....#........#.#.",
"........##.##....#####.#.#..##.",
"..##.#.#...#####..........#.#.#",
"#.........#......##...#.....#..",
".##.#........#...#..##...#...#.",
".......##..#...#.....#.##......",
"....#.#...##..##..#....##......",
"#........#..........##..####.#.",
"...###...#.#.###.#...#....#.#.#",
".....##.#.....#........#.#....#",
"#.......#....#...##..#......#..",
"...#..........#.#.#...#.#.###.#",
"....##.....#.##..#.#.#.........",
"#.##..##..#....#.........#...#.",
".###..........#...##.#..#......",
".....####.............##...###.",
".#..#....#..#...#..#...........",
"#..#..##..#...#.##..#.###.#...#",
"......#.#..###...#..#.....#..#.",
"##.##......#...#.#...#.........",
"....##.#.......#.#..##....#.#.#",
"#..##..#...###.#....##.........",
".............#.#....#...##..#..",
"..#....#...#.....#.##.#..##..##",
"##.#..##.#..##.#.#.##.#...#.#..",
".##.#..#.#........##.#...##....",
"#.........##....##..#......#...",
".#.#.......##...#..#......###.#",
"........#.#.#.#......#....#..#.",
"...##..#...#...#.##..#....#.#..",
"...#.#.#.#.......#.......###..#",
"...#..##..#####.#.....##.#..#..",
".......#.#.....#.....#...#...##",
"#...#...#......##.#....##......",
"#.....#.#.#.....#....#......#..",
"..#..#.##.#......##..#.#..#..##",
"####...#.....#....#.#..........",
"....#.....###...#...##......#..",
".....#....#...#............#...",
"...#...#..##.........#...#...##",
"#.#..#.#...##.#.......#..#.#...",
".#.....#...##.............#...#",
".....#..##..#....#......#.##..#",
"....#...###.................#..",
"...###...#....#...#...#........",
"....#.##.#.......#..#..........",
"...#..#......#.#...###...#.#...",
"..#.#..#...#.......#.......#.#.",
".#.#...#.#.##........#.........",
"...#..#...#....#.#.#.#.#..###..",
".#..##......#.#.##..#.##....#..",
"#....#.......##.....#.#........",
"..###..#.#.#.......##....#.....",
"........#.#.#....##...##..#....",
"#....##.#....#...##..##...#....",
"...#..##.#.....#...#.....##....",
".#.#..#..#...#....#..##.#....#.",
"##.#.##....#.....#....#....#.#.",
".##......#............##...#...",
"#..##.#.####.#.#....#..#..#.#.#",
"#...##...#......##....###.....#",
"..#.##.....#....#....#......#..",
".##.#...#.....#.#.#.#........##",
".#..#....#.#...........#...#...",
"#.....#..#.....#.#.##.#.....#..",
"....#.....#..#.#....###........",
".....###...........#.#..##.#.#.",
"....###....#.......###..#...#.#",
".###.....#...##.#...##........#",
"..#..#.#..#...#.#...#.#..#...#.",
"#.####.......#....##.#..#.#..#.",
"....#.#.##.#..###.........##.#.",
"..#..#.#....#....#.##..........",
"..##.###..#.#..#.#......#....#.",
".#..#.....##...#.#......##.#..#",
"#.#....#..#.#.#........#.###...",
"...#....##....##..###.###.#.#..",
"..#....#.....#....##.#.........",
"#.......#....#.........##..#...",
".#..#...#.#..#.#....#.#........",
"...#..###...#.....#......##....",
"..#...........#.....#..........",
"....###.#...#......#...#..#....",
".....#.##..#..#....#.......#..#",
"....##..#.#.#..............#.#.",
".#.#..#..#.#......#...#.#......",
"....#.......#.##....##.#.#.#..#",
"............#.#.#.....##.......",
"........#...##.#..#......#...##",
".........#...#...#....#...#.##.",
"..#.....#......#......#.....#..",
"#....#...##..#.#....#.#...#.###",
".......#..#..#..#.#...#.....#.#",
"...#.#...#......##.....#..#....",
"...#.#.####..##.#..#...........",
"..##..##....#.....####...#....#",
"###.......#...##.#...#...#...#.",
".##..#.....#..####......#....#.",
"#.....#..#..##..##...#..#..#...",
".#....#.....#...####..####.....",
"..#....#...#......#........#.#.",
"##.#.......#..#.....#..##..##..",
".#..#..#.#.#...#....##...#.##.#",
"##...#..#....#.........##......",    
]

def main(input):
    x = 0
    trees = 0
    for i in input:
        if x >= len(i):
            x-=len(i)
        print(i[x])
        if i[x] == "#":
            trees += 1
        x+=3
    return trees
    
print(main(input))
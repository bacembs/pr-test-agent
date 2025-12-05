# Copilot Instructions for HashTable TypeScript Project

## Project Overview
This repository implements a **HashTable data structure in TypeScript** with comprehensive unit tests. It demonstrates software engineering best practices including testing, linting, and type safety.

## Key Technologies
- **Language**: TypeScript 4.4+
- **Runtime**: Node.js 16+
- **Testing Framework**: Jest 27+
- **Linting**: ESLint with TypeScript support
- **Code Formatting**: Prettier
- **Build Tool**: TypeScript Compiler (tsc)

## Code Structure
```
pr-test-agent/
├── .github/
│   └── copilot-instructions.md   # This file
├── .vscode/                       # VS Code settings
├── .eslintrc.js                   # ESLint configuration
├── .prettierrc                    # Prettier formatting config
├── jest.config.js                 # Jest test configuration
├── tsconfig.json                  # TypeScript configuration
├── HashTable.ts                   # HashTable implementation
├── HashTable.spec.ts              # Jest unit tests
├── package.json                   # Project dependencies
└── yarn.lock                      # Yarn lock file
```

## Development Guidelines

### TypeScript Best Practices
1. **Type Safety**:
   - Always provide explicit type annotations for function parameters and returns
   - Use generics for reusable, type-safe data structures
   - Avoid `any` type unless absolutely necessary

2. **Code Style**:
   - Follow ESLint rules configured in `.eslintrc.js`
   - Use Prettier for consistent formatting
   - Run `yarn lint` to fix linting issues automatically
   - Variable/function names should be descriptive and camelCase

3. **Testing Requirements**:
   - Write Jest tests in `.spec.ts` files
   - Test file should be co-located with implementation
   - Aim for high test coverage (positive, negative, and edge cases)
   - Use `describe()` blocks to organize tests logically

### Common Commands
```bash
# Run tests
yarn test

# Lint and fix code
yarn lint

# Build TypeScript
yarn build

# Run tests in watch mode
yarn test --watch
```

### HashTable Implementation Notes
1. **Core Methods to Maintain**:
   - Constructor and initialization
   - `set(key, value)` - Insert or update
   - `get(key)` - Retrieve value
   - `delete(key)` - Remove entry
   - `has(key)` - Check existence
   - `clear()` - Remove all entries
   - `size` getter - Return entry count

2. **Collision Handling**:
   - Document collision resolution strategy (chaining vs. probing)
   - Ensure consistent behavior across all methods
   - Handle edge cases like null/undefined keys

3. **Performance Considerations**:
   - Hash function should distribute keys evenly
   - Resizing strategy when load factor exceeds threshold
   - Time complexity should be O(1) average case

### Testing Patterns
```typescript
describe('HashTable', () => {
  test('should add and retrieve values', () => {
    // Arrange, Act, Assert pattern
  });

  test('should handle collisions', () => {
    // Test specific collision scenario
  });

  test('should throw/handle edge cases', () => {
    // Test null, undefined, empty string keys
  });
});
```

### Best Practices
1. **Before committing**:
   - Run `yarn test` - all tests must pass
   - Run `yarn lint` - no linting errors
   - Run `yarn build` - TypeScript compiles without errors

2. **Commit Messages**:
   - Use conventional commits: `feat:`, `fix:`, `test:`, `docs:`
   - Be descriptive: `feat: implement collision resolution strategy`

3. **PR Review Focus**:
   - Type safety - are types properly defined?
   - Test coverage - are edge cases tested?
   - Performance - is the implementation efficient?
   - Documentation - is the code self-documenting?

### Troubleshooting
- **TypeScript errors**: Check `tsconfig.json` compilation options
- **Test failures**: Run `yarn test --verbose` for detailed output
- **Linting issues**: Run `yarn lint` to auto-fix most issues
- **Build errors**: Verify all dependencies are installed with `yarn install`

## When to Ask for Help
- Type definition questions
- Test case design and coverage
- Performance optimization strategies
- Algorithm implementation correctness
- TypeScript compiler error troubleshooting
